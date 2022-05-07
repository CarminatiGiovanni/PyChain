import React, {useState} from "react";


class App extends React.Component {

  constructor(props: any){
    super(props)
    const [address, setAddress] = useState('') // TODO: fix error
  }

  handleSubmit = (e: React.MouseEvent<HTMLFormElement>) => {
    e.preventDefault()

    const url_regex = "((http|https)://)(www.)?"
    + "[a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]"
    + "{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)"

    const address = (e.currentTarget.elements.namedItem("server address") as HTMLInputElement).value

    if(address.match(url_regex) != null){

    }
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