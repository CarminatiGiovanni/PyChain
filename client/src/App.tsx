import React, { MouseEventHandler } from "react";


class App extends React.Component {

  handleSubmit = (e: React.MouseEvent<HTMLFormElement>) => {
    e.preventDefault()

    console.log((e.currentTarget.elements.namedItem("server address") as HTMLInputElement).value)
  }

  render() {
      return (
        <div className="App">
          <form onSubmit={this.handleSubmit}>
            <input id="server_address" name="server address" placeholder="Server address:" type="text"/>
            <input id="submit_button" type="submit" placeholder="Save"/>
          </form>
        </div>
      );
  }
}

export default App