#!/bin/bash

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=xAIzaSyBJIsHjuoc_sgUug3yOQwxm_2274hZdp1Qx" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "contents": [{
    "parts":[{"text": "Explain how AI works"}]
    }]
   }'

