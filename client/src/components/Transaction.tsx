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
                    t.value.split('\n').map((l) => {
                        return <>{l} <br/> </>
                    })
                }
            </>
        case 'image':
            return <>Image</>
        default:
            return <></>
    }
}