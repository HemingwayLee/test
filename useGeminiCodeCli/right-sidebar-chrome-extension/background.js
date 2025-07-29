let sidebarOpen = false;

chrome.action.onClicked.addListener((tab) => {
  sidebarOpen = !sidebarOpen;

  if (sidebarOpen) {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ["sidebar.js"]
    });
  } else {
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        const sidebar = document.getElementById("right-sidebar-12345");
        if (sidebar) {
          sidebar.remove();
        }
      }
    });
  }
});