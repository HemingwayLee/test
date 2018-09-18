import React from 'react';

class App extends React.Component {
  render() {
    var myStyle = {
      fontSize: 36,
      color: "#FF0000"
    }

    var url = window.location.href;

    var a = true;
    return (
      // this is JavaScript Expressions
      <div style={myStyle}>
        Hello { a ? url : "World" }
      </div>
    );
  }
}

export default App;