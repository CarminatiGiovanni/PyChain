import "./../style/css/block.css"
import { BlockInterface } from "./../classes";
import { Popover, Modal, Button } from "react-bootstrap";
import { useState } from "react";
import TransactionList from "./TransactionList";

export const Block = ({block} : {block: BlockInterface}) => {
    const {index,prevHash,timestamp,hash} = block
    const [show, setShow] = useState(false);
  
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);


    return(
        <>
            <Button variant='danger' className="block" onClick={handleShow}>
                <p className="hash" onClick={() => alert(hash)}>
                    {hash.substring(0,16) + '...'}
                </p>
                <p className="index"> index: &ensp;&ensp;&ensp; <b className="index">{index}</b></p>
                <p onClick={() => alert(prevHash)}>prevHash:  <h1  className="prevHash" >{prevHash.substring(0,16) + '...'}</h1></p>
                <p>timestamp:<h1 className="timestamp"> {timestamp}</h1></p>
            </Button>

            <Modal show={show} onHide={handleClose}>
                <Modal.Header closeButton>
                <Modal.Title>Block: {block.index}</Modal.Title>
                </Modal.Header>
                <Modal.Body>
                    <TransactionList transactions={block.transactions}/>
                </Modal.Body>
                <Modal.Footer>
                <Button variant="primary" onClick={handleClose}>
                    Close
                </Button>
                </Modal.Footer>
            </Modal>
        </>
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