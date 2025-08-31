document.addEventListener('DOMContentLoaded', function() {
  const youtubeUrlInput = document.getElementById('youtubeUrlInput');
  const addUrlBtn = document.getElementById('addUrlBtn');
  const urlList = document.getElementById('urlList');
  const pagination = document.getElementById('pagination');
  const currentTimeElement = document.getElementById('currentTime');
  const tabInfoElement = document.getElementById('tabInfo');

  let currentPage = 1;
  const urlsPerPage = 5;
  let allUrls = [];

  function isValidYouTubeUrl(url) {
    const youtubeRegex = /^(https?\:\/\/)?(www\.)?(youtube\.com|youtu\.be)\/.+/;
    return youtubeRegex.test(url);
  }

  function extractVideoId(url) {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
    const match = url.match(regExp);
    return (match && match[2].length === 11) ? match[2] : null;
  }

  async function getYouTubeSubtitles(videoId) {
    return new Promise((resolve, reject) => {
      chrome.runtime.sendMessage(
        { action: 'getYouTubeSubtitles', videoId: videoId },
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

    if (allUrls.some(item => (typeof item === 'string' ? item : item.url) === url)) {
      alert('URL already exists');
      return;
    }

    addUrlBtn.disabled = true;
    addUrlBtn.textContent = 'Getting subtitles...';

    const videoId = extractVideoId(url);
    let subtitles = null;
    
    if (videoId) {
      subtitles = await getYouTubeSubtitles(videoId);
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
            <button class="delete-btn" data-url="${url}" data-index="${startIndex + index}">Delete</button>
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
  
  youtubeUrlInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
      addUrl();
    }
  });

  loadUrlsFromStorage();
  updateTime();
  updateTabInfo();

  setInterval(updateTime, 1000);
  setInterval(updateTabInfo, 5000);
});