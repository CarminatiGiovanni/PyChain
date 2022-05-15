import {useState, useContext, useEffect} from "react";
import { BlockchainContext } from "./App";
import { BlockchainJSONInterface } from "./classes";
import { Block } from "./components/Block";
import './style/css/server_address.css'
import './style/css/block.css'

const Blockchain = () => {

  const {blockchain} = useContext(BlockchainContext)

  return (
    <>
        <div className="container">
        {
          ((blockchain as BlockchainJSONInterface)['blockchain']).slice().reverse().map((block) => {
            return (
              <Block key={block.index} block = {block}/>
            )
          })
        }
        </div>
    </>
  );
}

export default Blockchain