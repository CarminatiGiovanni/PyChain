import "./../style/css/block.css"
import { BlockInterface } from "./../classes";
import { Popover, OverlayTrigger, Button } from "react-bootstrap";
import TransactionList from "./TransactionList";

export const Block = ({block} : {block: BlockInterface}) => {
    const {index,prevHash,timestamp,hash} = block   
    return(
        <Button variant='danger' className="block">
            <p className="hash" onClick={() => alert(hash)}>
                {hash.substring(0,16) + '...'}
            </p>
            <p className="index"> index: &ensp;&ensp;&ensp; <b className="index">{index}</b></p>
            <p onClick={() => alert(prevHash)}>prevHash:  <h1  className="prevHash" >{prevHash.substring(0,16) + '...'}</h1></p>
            <p>timestamp:<h1 className="timestamp"> {timestamp}</h1></p>
        </Button>
    )
}

const popover = (block: BlockInterface) => {
    return (
        <Popover id="popover-basic">
        <Popover.Header as="h3">Block: {block.index}</Popover.Header>
        <Popover.Body>
            jfiohjidf9
        </Popover.Body>
        </Popover>
  )}