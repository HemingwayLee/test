document.addEventListener('DOMContentLoaded', function() {
  const refreshBtn = document.getElementById('refreshBtn');
  const settingsBtn = document.getElementById('settingsBtn');
  const currentTimeElement = document.getElementById('currentTime');
  const tabInfoElement = document.getElementById('tabInfo');

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

  function refreshContent() {
    updateTime();
    updateTabInfo();
    
    refreshBtn.textContent = 'Refreshing...';
    refreshBtn.disabled = true;
    
    setTimeout(() => {
      refreshBtn.textContent = 'Refresh Content';
      refreshBtn.disabled = false;
    }, 1000);
  }

  function openSettings() {
    alert('Settings functionality would be implemented here!');
  }

  refreshBtn.addEventListener('click', refreshContent);
  settingsBtn.addEventListener('click', openSettings);

  updateTime();
  updateTabInfo();

  setInterval(updateTime, 1000);
  
  setInterval(updateTabInfo, 5000);
});