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

  function addUrl() {
    const url = youtubeUrlInput.value.trim();
    
    if (!url) {
      alert('Please enter a URL');
      return;
    }

    if (!isValidYouTubeUrl(url)) {
      alert('Please enter a valid YouTube URL');
      return;
    }

    if (allUrls.includes(url)) {
      alert('URL already exists');
      return;
    }

    allUrls.unshift(url);
    saveUrlsToStorage(allUrls);
    youtubeUrlInput.value = '';
    currentPage = 1;
    displayUrls();
  }

  function deleteUrl(url) {
    allUrls = allUrls.filter(savedUrl => savedUrl !== url);
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
      urlList.innerHTML = urlsToShow.map((url, index) => `
        <div class="url-item">
          <div class="url-text">
            <a href="${url}" target="_blank">${url}</a>
          </div>
          <button class="delete-btn" data-url="${url}" data-index="${startIndex + index}">Delete</button>
        </div>
      `).join('');
      
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