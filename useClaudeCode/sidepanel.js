document.addEventListener('DOMContentLoaded', function() {
  const youtubeUrlInput = document.getElementById('youtubeUrlInput');
  const addUrlBtn = document.getElementById('addUrlBtn');
  const urlList = document.getElementById('urlList');
  const pagination = document.getElementById('pagination');
  const currentTimeElement = document.getElementById('currentTime');
  const tabInfoElement = document.getElementById('tabInfo');
  const languageSelect = document.getElementById('languageSelect');

  const serverUrlInput = document.getElementById('serverUrlInput');
  const addServerBtn = document.getElementById('addServerBtn');
  const serverList = document.getElementById('serverList');
  const serverStatus = document.getElementById('serverStatus');

  const geminiApiKeyInput = document.getElementById('geminiApiKeyInput');
  const saveApiKeyBtn = document.getElementById('saveApiKeyBtn');
  const clearApiKeyBtn = document.getElementById('clearApiKeyBtn');
  const apiKeyStatus = document.getElementById('apiKeyStatus');

  const tabButtons = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');

  let currentPage = 1;
  const urlsPerPage = 5;
  let allUrls = [];
  let configuredServers = [];

  function switchTab(tabName) {
    tabButtons.forEach(btn => btn.classList.remove('active'));
    tabContents.forEach(content => content.classList.remove('active'));
    
    document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
    document.getElementById(`${tabName}-tab`).classList.add('active');
  }

  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const tabName = button.getAttribute('data-tab');
      switchTab(tabName);
    });
  });

  function isValidServerUrl(url) {
    const serverRegex = /^(?:https?:\/\/)?(?:\d{1,3}\.){3}\d{1,3}:\d+$|^(?:https?:\/\/)?localhost:\d+$/;
    return serverRegex.test(url);
  }

  function saveServersToStorage(servers) {
    chrome.storage.local.set({ 'configuredServers': servers }, function() {
      if (chrome.runtime.lastError) {
        console.error('Error saving servers:', chrome.runtime.lastError);
      }
    });
  }

  function loadServersFromStorage() {
    chrome.storage.local.get(['configuredServers'], function(result) {
      if (chrome.runtime.lastError) {
        console.error('Error loading servers:', chrome.runtime.lastError);
        return;
      }
      configuredServers = result.configuredServers || [];
      displayServers();
    });
  }

  function addServer() {
    const serverUrl = serverUrlInput.value.trim();
    
    if (!serverUrl) {
      alert('Please enter a server URL');
      return;
    }

    let formattedUrl = serverUrl;
    if (!formattedUrl.includes('://')) {
      formattedUrl = 'http://' + formattedUrl;
    }

    if (!isValidServerUrl(formattedUrl)) {
      alert('Please enter a valid server URL (e.g., 127.0.0.1:5000 or localhost:5000)');
      return;
    }

    if (configuredServers.some(server => server.url === formattedUrl)) {
      alert('Server already exists');
      return;
    }

    const serverObject = {
      url: formattedUrl,
      name: formattedUrl.replace(/^https?:\/\//, ''),
      dateAdded: new Date().toISOString(),
      active: configuredServers.length === 0
    };

    configuredServers.push(serverObject);
    saveServersToStorage(configuredServers);
    serverUrlInput.value = '';
    displayServers();
    updateServerStatus();
  }

  function deleteServer(url) {
    configuredServers = configuredServers.filter(server => server.url !== url);
    if (configuredServers.length > 0 && !configuredServers.some(server => server.active)) {
      configuredServers[0].active = true;
    }
    saveServersToStorage(configuredServers);
    displayServers();
    updateServerStatus();
  }

  function setActiveServer(url) {
    configuredServers.forEach(server => {
      server.active = server.url === url;
    });
    saveServersToStorage(configuredServers);
    displayServers();
    updateServerStatus();
  }

  function displayServers() {
    if (configuredServers.length === 0) {
      serverList.innerHTML = '<p style="color: #666; text-align: center; padding: 20px;">No servers configured</p>';
    } else {
      serverList.innerHTML = configuredServers.map(server => {
        const dateAdded = new Date(server.dateAdded).toLocaleDateString();
        return `
          <div class="server-item ${server.active ? 'active' : ''}">
            <div class="server-info">
              <div class="server-url">${server.name}</div>
              <small style="color: #666;">Added: ${dateAdded}</small>
            </div>
            <div class="server-actions">
              ${!server.active ? `<button class="activate-btn" onclick="setActiveServer('${server.url}')">Activate</button>` : '<span class="active-badge">Active</span>'}
              <button class="delete-btn" onclick="deleteServer('${server.url}')">Delete</button>
            </div>
          </div>
        `;
      }).join('');
    }
  }

  function updateServerStatus() {
    const activeServer = configuredServers.find(server => server.active);
    if (activeServer) {
      serverStatus.innerHTML = `<strong>Active Server:</strong> ${activeServer.name}`;
    } else {
      serverStatus.innerHTML = 'No active server configured';
    }
  }

  window.setActiveServer = setActiveServer;
  window.deleteServer = deleteServer;

  function saveGeminiApiKey() {
    const apiKey = geminiApiKeyInput.value.trim();
    
    if (!apiKey) {
      alert('Please enter an API key');
      return;
    }

    if (apiKey.length < 10) {
      alert('Please enter a valid API key');
      return;
    }

    chrome.storage.local.set({ 'geminiApiKey': apiKey }, function() {
      if (chrome.runtime.lastError) {
        console.error('Error saving API key:', chrome.runtime.lastError);
        alert('Error saving API key');
        return;
      }
      
      geminiApiKeyInput.value = '';
      updateApiKeyStatus();
      alert('Gemini API key saved successfully');
    });
  }

  function clearGeminiApiKey() {
    if (confirm('Are you sure you want to clear the API key?')) {
      chrome.storage.local.remove(['geminiApiKey'], function() {
        if (chrome.runtime.lastError) {
          console.error('Error clearing API key:', chrome.runtime.lastError);
          return;
        }
        updateApiKeyStatus();
        alert('API key cleared successfully');
      });
    }
  }

  function loadGeminiApiKey() {
    chrome.storage.local.get(['geminiApiKey'], function(result) {
      if (chrome.runtime.lastError) {
        console.error('Error loading API key:', chrome.runtime.lastError);
        return;
      }
      updateApiKeyStatus(result.geminiApiKey);
    });
  }

  function updateApiKeyStatus(apiKey = null) {
    if (apiKey === null) {
      chrome.storage.local.get(['geminiApiKey'], function(result) {
        if (chrome.runtime.lastError) {
          console.error('Error checking API key:', chrome.runtime.lastError);
          return;
        }
        displayApiKeyStatus(result.geminiApiKey);
      });
    } else {
      displayApiKeyStatus(apiKey);
    }
  }

  function displayApiKeyStatus(apiKey) {
    if (apiKey) {
      const maskedKey = apiKey.substring(0, 8) + '...' + apiKey.substring(apiKey.length - 4);
      apiKeyStatus.innerHTML = `<span style="color: #4CAF50;">✓ API key configured: ${maskedKey}</span>`;
    } else {
      apiKeyStatus.innerHTML = '<span style="color: #f44336;">No API key configured</span>';
    }
  }




  function isValidYouTubeUrl(url) {
    const youtubeRegex = /^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/.+/;
    return youtubeRegex.test(url);
  }

  function extractVideoId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
  }

  async function getYouTubeSubtitles(videoId, language = 'en') {
    return new Promise((resolve, reject) => {
      chrome.runtime.sendMessage(
        { action: 'getYouTubeSubtitles', videoId: videoId, language: language },
        (response) => {
          if (response.success) {
            resolve(response.subtitles);
          } else {
            reject(new Error(response.error));
          }
        }
      );
    });
  }

  function saveUrlsToStorage(urls) {
    chrome.storage.local.set({ 'youtubeUrls': urls }, function() {
      if (chrome.runtime.lastError) {
        console.error('Error saving URLs:', chrome.runtime.lastError);
      }
    });
  }

  function loadUrlsFromStorage() {
    chrome.storage.local.get(['youtubeUrls'], function(result) {
      if (chrome.runtime.lastError) {
        console.error('Error loading URLs:', chrome.runtime.lastError);
        return;
      }
      allUrls = result.youtubeUrls || [];
      displayUrls();
    });
  }

  async function addUrl() {
    const url = youtubeUrlInput.value.trim();
    
    if (!url) {
      alert('Please enter a URL');
      return;
    }

    if (!isValidYouTubeUrl(url)) {
      alert('Please enter a valid YouTube URL');
      return;
    }

    // Ensure URLs are loaded from storage before checking duplicates
    await new Promise((resolve) => {
      chrome.storage.local.get(['youtubeUrls'], function(result) {
        if (!chrome.runtime.lastError) {
          allUrls = result.youtubeUrls || [];
        }
        resolve();
      });
    });

    if (allUrls.some(item => (typeof item === 'string' ? item : item.url) === url)) {
      alert('URL already exists');
      displayUrls(); // Display the loaded URLs
      return;
    }

    addUrlBtn.disabled = true;
    addUrlBtn.textContent = 'Getting subtitles...';

    const videoId = extractVideoId(url);
    const selectedLanguage = languageSelect.value;
    let subtitles = null;
    
    if (videoId) {
      subtitles = await getYouTubeSubtitles(videoId, selectedLanguage);
    }

    const urlObject = {
      url: url,
      subtitles: subtitles,
      dateAdded: new Date().toISOString()
    };

    allUrls.unshift(urlObject);
    saveUrlsToStorage(allUrls);
    youtubeUrlInput.value = '';
    currentPage = 1;
    displayUrls();

    addUrlBtn.disabled = false;
    addUrlBtn.textContent = 'Add URL';
  }

  function deleteUrl(url) {
    allUrls = allUrls.filter(item => (typeof item === 'string' ? item : item.url) !== url);
    saveUrlsToStorage(allUrls);
    
    const totalPages = Math.ceil(allUrls.length / urlsPerPage);
    if (currentPage > totalPages && totalPages > 0) {
      currentPage = totalPages;
    }
    
    displayUrls();
  }

  function summarizeUrl(url) {
    // Find the URL item to get subtitles
    const urlItem = allUrls.find(item => (typeof item === 'string' ? item : item.url) === url);
    
    if (!urlItem || !urlItem.subtitles) {
      alert('No subtitles available for this video to summarize');
      return;
    }
    
    // For now, just show an alert with a placeholder message
    // This function can be extended later to integrate with AI services
    alert('Summarize feature clicked for: ' + url + '\nSubtitles length: ' + urlItem.subtitles.length + ' characters');
  }

  function displayUrls() {
    const startIndex = (currentPage - 1) * urlsPerPage;
    const endIndex = startIndex + urlsPerPage;
    const urlsToShow = allUrls.slice(startIndex, endIndex);

    if (urlsToShow.length === 0) {
      urlList.innerHTML = '<p style="color: #666; text-align: center; padding: 20px;">No YouTube URLs saved yet</p>';
    } else {
      urlList.innerHTML = urlsToShow.map((item, index) => {
        const url = typeof item === 'string' ? item : item.url;
        const subtitles = typeof item === 'object' && item.subtitles ? item.subtitles : null;
        const dateAdded = typeof item === 'object' && item.dateAdded ? new Date(item.dateAdded).toLocaleDateString() : '';
        
        return `
          <div class="url-item">
            <div class="url-text">
              <a href="${url}" target="_blank">${url}</a>
              ${dateAdded ? `<small style="color: #666; display: block;">Added: ${dateAdded}</small>` : ''}
              ${subtitles ? `<details style="margin-top: 8px;"><summary style="cursor: pointer; color: #007acc;">Subtitles</summary><div style="max-height: 150px; overflow-y: auto; padding: 8px; background: #f5f5f5; border-radius: 4px; font-size: 12px; margin-top: 4px;">${subtitles}</div></details>` : '<small style="color: #999;">No subtitles available</small>'}
            </div>
            <div class="button-group">
              <button class="delete-btn" data-url="${url}" data-index="${startIndex + index}">Delete</button>
              <button class="summarize-btn" data-url="${url}" data-index="${startIndex + index}">Summarize</button>
            </div>
          </div>
        `;
      }).join('');
      
      // Add event listeners to delete buttons
      const deleteButtons = urlList.querySelectorAll('.delete-btn');
      deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
          const url = this.getAttribute('data-url');
          deleteUrl(url);
        });
      });

      // Add event listeners to summarize buttons
      const summarizeButtons = urlList.querySelectorAll('.summarize-btn');
      summarizeButtons.forEach(button => {
        button.addEventListener('click', function() {
          const url = this.getAttribute('data-url');
          summarizeUrl(url);
        });
      });
    }

    displayPagination();
  }

  function displayPagination() {
    const totalPages = Math.ceil(allUrls.length / urlsPerPage);
    
    if (totalPages <= 1) {
      pagination.innerHTML = '';
      return;
    }

    pagination.innerHTML = `
      <button class="prev-btn" ${currentPage === 1 ? 'disabled' : ''} data-page="${currentPage - 1}">Previous</button>
      <span class="page-info">Page ${currentPage} of ${totalPages}</span>
      <button class="next-btn" ${currentPage === totalPages ? 'disabled' : ''} data-page="${currentPage + 1}">Next</button>
    `;
    
    // Add event listeners to pagination buttons
    const prevBtn = pagination.querySelector('.prev-btn');
    const nextBtn = pagination.querySelector('.next-btn');
    
    if (prevBtn && !prevBtn.disabled) {
      prevBtn.addEventListener('click', function() {
        const page = parseInt(this.getAttribute('data-page'));
        changePage(page);
      });
    }
    
    if (nextBtn && !nextBtn.disabled) {
      nextBtn.addEventListener('click', function() {
        const page = parseInt(this.getAttribute('data-page'));
        changePage(page);
      });
    }
  }

  function changePage(page) {
    const totalPages = Math.ceil(allUrls.length / urlsPerPage);
    if (page >= 1 && page <= totalPages) {
      currentPage = page;
      displayUrls();
    }
  }

  function deleteUrlHandler(url) {
    deleteUrl(url);
  }

  function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleString();
    currentTimeElement.textContent = `Current time: ${timeString}`;
  }

  function updateTabInfo() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      if (tabs[0]) {
        const tab = tabs[0];
        tabInfoElement.innerHTML = `
          <strong>Current Tab:</strong><br>
          Title: ${tab.title}<br>
          URL: ${tab.url}
        `;
      }
    });
  }

  addUrlBtn.addEventListener('click', addUrl);
  addServerBtn.addEventListener('click', addServer);
  saveApiKeyBtn.addEventListener('click', saveGeminiApiKey);
  clearApiKeyBtn.addEventListener('click', clearGeminiApiKey);
  
  youtubeUrlInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      addUrl();
    }
  });

  serverUrlInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      addServer();
    }
  });

  geminiApiKeyInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      saveGeminiApiKey();
    }
  });

  loadUrlsFromStorage();
  loadServersFromStorage();
  loadGeminiApiKey();
  updateTime();
  updateTabInfo();
  updateServerStatus();

  setInterval(updateTime, 1000);
  setInterval(updateTabInfo, 5000);
});