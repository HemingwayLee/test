import os
import openai
import mido

with open('.env') as f:
    for line in f:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value

# print(os.environ["API_KEY"])


openai.api_key = os.environ["API_KEY"]

model_engine = "text-davinci-002"
max_tokens = 2048

prompt = "Play a happy song"
temperature = 0.7
top_p = 1
n = 1
stop = "\n\n"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=max_tokens,
    n=n,
    temperature=temperature,
    top_p=top_p,
    stop=stop,
)

message = completions.choices[0].text.strip()
print(message)


# Define some constants
PPQ = 480  # pulses per quarter note
DEFAULT_VELOCITY = 64

# Create a MIDI file object
mid = mido.MidiFile(ticks_per_beat=PPQ)

# Add a track to the MIDI file
track = mido.MidiTrack()
mid.tracks.append(track)

# Split the message into lines
lines = message.strip().split('\n')

print(lines)

# Loop over each line and parse the commands
for line in lines:
    parts = line.split()
    if parts[0] == 'note':
        # Parse note commands: note channel pitch velocity time
        channel = int(parts[1])
        pitch = int(parts[2])
        velocity = int(parts[3]) if len(parts) > 3 else DEFAULT_VELOCITY
        time = int(float(parts[4]) * PPQ)
        # Add a note on event
        track.append(mido.Message('note_on', note=pitch, velocity=velocity, time=time, channel=channel))
    elif parts[0] == 'rest':
        # Parse rest commands: rest time
        time = int(float(parts[1]) * PPQ)
        # Add a note off event
        track.append(mido.Message('note_off', note=0, velocity=0, time=time))
    elif parts[0] == 'tempo':
        # Parse tempo commands: tempo value
        value = int(float(parts[1]))
        # Add a tempo event
        track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(value)))
    elif parts[0] == 'time_signature':
        # Parse time signature commands: time_signature numerator denominator clocks_per_tick
        numerator = int(parts[1])
        denominator = int(parts[2])
        clocks_per_tick = int(parts[3])
        # Add a time signature event
        track.append(mido.MetaMessage('time_signature', numerator=numerator, denominator=denominator, clocks_per_click=clocks_per_tick))

# Save the MIDI file to disk
mid.save('output.mid')


