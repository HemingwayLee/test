#!/bin/bash

base_tr=$1
max_iters=$2
version=$3
folder=$4

echo "base_tr: ${base_tr}"
echo "max_iters: ${max_iters}"
echo "version: ${version}"
echo "folder: ${folder}"

echo "----- download traineddata -----"
if [ ! -d /root/models/langdata_lstm ]; then
  git clone --depth 1 https://github.com/tesseract-ocr/langdata_lstm.git /root/models/langdata_lstm
fi

if [ ! -d /root/models/tesseract ]; then
  git clone --depth 1 https://github.com/tesseract-ocr/tesseract.git /root/models/tesseract
fi

if [ ! -f /root/models/tesseract/tessdata/eng.traineddata ]; then
  wget https://github.com/tesseract-ocr/tessdata/raw/master/eng.traineddata -P /root/models/tesseract/tessdata/
fi

if [ ! -f /root/models/tesseract/tessdata/jpn.traineddata ]; then
  wget https://github.com/tesseract-ocr/tessdata/raw/master/jpn.traineddata -P /root/models/tesseract/tessdata/
fi

mkdir -p /root/traintess/lstm
mkdir -p /root/traintess/checkpoints
mkdir -p /root/traintess/training_data

echo "----- make lstmf files -----"
cp -R /root/training_data/$folder/* /root/traintess/training_data
cd /root/traintess/training_data
for file in *.tif; do
  base=`basename $file .tif`
  TESSDATA_PREFIX=/root/models/tesseract/tessdata tesseract $file $base lstm.train
done

echo "----- make text file to contain lstmf files -----"
cat > $folder.training_file.txt
for i in *.lstmf; do
  echo "$i" >> $folder.training_file.txt
done
cat $folder.training_file.txt

cp /root/models/tesseract/tessdata/$base_tr.traineddata /root/output/
combine_tessdata -e /root/output/$base_tr.traineddata /root/traintess/lstm/$base_tr.lstm

echo "----- do training -----"
echo "aaa"
ls -l /root/traintess/checkpoints/

lstmtraining \
  --model_output /root/traintess/checkpoints/$folder \
  --continue_from /root/traintess/lstm/$base_tr.lstm \
  --traineddata /root/output/$base_tr.traineddata \
  --train_listfile /root/traintess/training_data/$folder.training_file.txt \
  --max_iterations $max_iters

echo "bbb"
ls -l /root/traintess/checkpoints/

lstmtraining \
  --stop_training \
  --continue_from /root/traintess/checkpoints/${folder}_checkpoint \
  --traineddata /root/output/$base_tr.traineddata \
  --model_output /root/output/${folder}${version}.traineddata

echo "ccc"
ls -l /root/traintess/checkpoints/

lstmeval \
  --verbosity 2 \
  --model /root/traintess/checkpoints/${folder}_checkpoint \
  --traineddata /root/output/$base_tr.traineddata \
  --eval_listfile /root/traintess/training_data/$folder.training_file.txt

rm -fr /root/traintess

