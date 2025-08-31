// Enable the side panel on extension startup
chrome.sidePanel
  .setPanelBehavior({ openPanelOnActionClick: true })
  .catch((error) => console.error(error));

chrome.runtime.onInstalled.addListener(() => {
  console.log('Side Panel Extension installed');
});

// YouTube transcript extraction functions using improved methods
async function extractVideoId(url) {
  const videoIdRegex = /(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})/;
  const match = url.match(videoIdRegex);
  return match ? match[1] : null;
}

async function getYouTubeVideoPage(videoId) {
  try {
    const response = await fetch(`https://www.youtube.com/watch?v=${videoId}`, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch video page: ${response.status}`);
    }
    
    return await response.text();
  } catch (error) {
    console.error('Error fetching video page:', error);
    throw error;
  }
}

async function extractCaptionTracks(html) {
  try {
    // Extract ytInitialPlayerResponse from the page - try multiple patterns
    let playerResponseMatch = html.match(/var ytInitialPlayerResponse = (\{.*?\});/);
    if (!playerResponseMatch) {
      playerResponseMatch = html.match(/"ytInitialPlayerResponse"\s*:\s*(\{.*?\})(?=\s*[,}])/);
    }
    if (!playerResponseMatch) {
      playerResponseMatch = html.match(/ytInitialPlayerResponse"?\s*[=:]\s*(\{.*?\})(?=[,;}])/);
    }
    if (!playerResponseMatch) {
      console.log('Could not find ytInitialPlayerResponse');
      return [];
    }

    const playerResponse = JSON.parse(playerResponseMatch[1]);
    
    // Navigate to captions data
    const captions = playerResponse?.captions?.playerCaptionsTracklistRenderer?.captionTracks;
    
    if (!captions || captions.length === 0) {
      console.log('No captions found in player response');
      return [];
    }

    return captions.map(caption => ({
      languageCode: caption.languageCode,
      name: caption.name?.simpleText || caption.languageCode,
      url: caption.baseUrl,
      isAutomatic: caption.kind === 'asr'
    }));
  } catch (error) {
    console.error('Error extracting caption tracks:', error);
    return [];
  }
}

async function fetchTranscriptFromUrl(url) {
  try {
    const response = await fetch(url, {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
      }
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch transcript: ${response.status}`);
    }
    
    const xmlText = await response.text();

    console.log("the text is ...")
    console.log(xmlText)
    
    // Parse XML to extract text content - handle CDATA and HTML entities
    const textMatches = xmlText.match(/<text[^>]*>.*?<\/text>/gs) || [];
    
    if (textMatches.length === 0) {
      console.log('No text content found in transcript XML');
      return null;
    }
    
    const transcriptText = textMatches
      .map(match => {
        // Extract content between <text> tags, handling CDATA and nested content
        const textContent = match.match(/<text[^>]*>(.*?)<\/text>/s);
        if (!textContent) return '';
        
        let text = textContent[1];
        
        // Handle CDATA sections
        text = text.replace(/<!\[CDATA\[(.*?)\]\]>/gs, '$1');
        
        // Remove any nested XML tags
        text = text.replace(/<[^>]+>/g, '');
        
        return text;
      })
      .filter(text => text.trim().length > 0)
      .join(' ')
      .replace(/&amp;/g, '&')
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/&quot;/g, '"')
      .replace(/&#39;/g, "'")
      .replace(/&#x27;/g, "'")
      .replace(/\s+/g, ' ')
      .trim();
    
    return transcriptText;
  } catch (error) {
    console.error('Error fetching transcript from URL:', error);
    return null;
  }
}

async function getYouTubeSubtitles(videoId) {
  try {
    console.log(`Fetching subtitles for video ID: ${videoId}`);
    
    // Get the video page HTML
    const html = await getYouTubeVideoPage(videoId);
    
    // Extract caption tracks from the HTML
    const captionTracks = await extractCaptionTracks(html);
    
    if (captionTracks.length === 0) {
      console.log('No caption tracks found for this video');
      return null;
    }
    
    console.log(`Found ${captionTracks.length} caption tracks:`, 
      captionTracks.map(track => `${track.name} (${track.languageCode})`).join(', '));
    
    // Prefer manual captions over automatic ones
    const manualCaptions = captionTracks.filter(track => !track.isAutomatic);
    const selectedTrack = manualCaptions.length > 0 ? manualCaptions[0] : captionTracks[0];
    
    console.log(`Using caption track: ${selectedTrack.name} (${selectedTrack.languageCode})`);
    
    // Fetch the transcript
    const transcript = await fetchTranscriptFromUrl(selectedTrack.url);
    
    if (transcript) {
      console.log('Successfully extracted transcript');
      return transcript;
    } else {
      console.log('Failed to extract transcript content');
      return null;
    }
    
  } catch (error) {
    console.error('Error in getYouTubeSubtitles:', error);
    return null;
  }
}

// Message handler
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'getYouTubeSubtitles') {
    getYouTubeSubtitles(request.videoId).then(subtitles => {
      sendResponse({ success: true, subtitles: subtitles });
    }).catch(error => {
      sendResponse({ success: false, error: error.message });
    });
    return true; // Keep the message channel open for async response
  }
});
