const sidebar = document.createElement('iframe');
sidebar.id = "right-sidebar-12345";
sidebar.src = chrome.runtime.getURL('sidebar.html');
sidebar.style.cssText = `
  position: fixed;
  top: 0;
  right: 0;
  width: 300px;
  height: 100%;
  border: 1px solid #ccc;
  z-index: 9999;
`;

document.body.appendChild(sidebar);