function getTabelogLink(content) {
  var hrefs = content.match(/href="([^"]*)/g);
  
  var url = "";
  for (var i = 0; i < hrefs.length; i++) {
    //url = ;
    if (hrefs[i].indexOf('https://tabelog.com') != -1) {
      return hrefs[i].substring(hrefs[i].indexOf('https://tabelog.com'));
    }
  }
  
  return "";
}

//Can not use the library: https://github.com/ConfidentCannabis/sheets-script-xpath
// because it is for XML not HTML
function getNearestStation(url) {
  var response = UrlFetchApp.fetch(url).getContentText();
  var pos = response.search('<th>交通手段</th>');
  if (pos >= 0) {
    var open = response.indexOf('<td>', pos);
    var close = response.indexOf('</td>', pos);
    return response.substring(open + 4, close).replace(/\s/g, '').replace(/(?:\r\n|\r|\n)/g, '');
  }
  
  return "";
}

function getData(sheetName, status) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  //var sheets = ss.getSheets();
  //var sheet = ss.getActiveSheet();
  var sheet = ss.getSheetByName(sheetName)

  var next = "";
  var len = 0;
  do {
    var url = "https://www.googleapis.com/blogger/v3/blogs/38280655509272816/posts?key=AIzaSyBJh2nohMG330Kc_tUM149dUrGuYS5bKwU&status=" + status + next;
    var response = UrlFetchApp.fetch(url);
    var data = JSON.parse(response.getContentText());
    
    var items = data.items;
    
    var rows = [], item, content, imageCount, tabelog, station, title, tags;
    for (i = 0; i < items.length; i++) {
      item = items[i];
      
      //remove html tags and line breaks
      title = item.title.replace(/<(?:.|\n)*?>/gm, '').replace(/(\r\n\t|\n|\r\t)/gm,"");
      content = item.content.replace(/<(?:.|\n)*?>/gm, '').replace(/(\r\n\t|\n|\r\t)/gm,"");
      
      //get the number of photos in content
      imageCount = (item.content.match(/<img/g) || []).length;
      
      tabelog = getTabelogLink(item.content);
      
      if (tabelog != "") { 
        station = getNearestStation(tabelog); 
      } else {
        station = "";
      }
      
      tags = JSON.stringify(item.labels).replace(/[\[\]"]/g, '');
      
      rows.push([title, content.length, imageCount, item.url, tabelog, tags, station]);
    }
    
    //start from the 2nd row because the 1st row is for title
    var dataRange = sheet.getRange(2 + len, 1, rows.length, 7);
    dataRange.setValues(rows);
    
    if (data.hasOwnProperty('nextPageToken')) {
      next = "&pageToken=" + data.nextPageToken;
      len = len + items.length;
    }
  } while(data.hasOwnProperty('nextPageToken'));
}

function getStarted() {
  getData("Dashboard", "live");
  
  //404 not found
  //getData("Draft", "draft");
}
