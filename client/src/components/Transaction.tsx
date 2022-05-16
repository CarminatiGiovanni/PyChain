import { TransactionInterface } from "../classes"
import { Dropdown } from "react-bootstrap"
import { useState } from "react"

const Transaction = ({transaction} : {transaction: TransactionInterface}) => {
    const [show,setShow] = useState<boolean>(false)

    return(
        <Dropdown className="d-inline mx-2" show={show} onMouseEnter={() => setShow(true)} onMouseLeave={() => setShow(false)}>
            <Dropdown.Toggle id="dropdown-autoclose-outside">
                {transaction.title}
            </Dropdown.Toggle>
            <Dropdown.Menu>
                <Dropdown.Item>
                    <b>{transaction.description}</b>
                </Dropdown.Item>
                <Dropdown.Item>
                    {
                        content(transaction)                    
                    }
                </Dropdown.Item>
                <Dropdown.Item>
                    <b>{transaction.author}</b>
                </Dropdown.Item>
                <Dropdown.Item style={{color:'lightblue'}}>
                    added to blockchian: {(new Date(transaction.timestamp * 1000)).toDateString()}
                </Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
    )
}

export default Transaction

const content = (t: TransactionInterface) => {
    switch(t.content_type){
        case 'text':
            return <>
                {
                    t.value.split('\n').map((l, index) => {
                        return <div key={index} >{l} <br/> </div>
                    })
                }
            </>
        case 'image':
            return <img className="d-inline-block" src={t.value} style={{maxWidth:'100%',maxHeight: '100%'}}/>
        default:
            return <></>
    }
}