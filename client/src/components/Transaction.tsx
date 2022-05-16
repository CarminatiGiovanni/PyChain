import { TransactionInterface } from "../classes"
import { Dropdown } from "react-bootstrap"


const Transaction = ({transaction} : {transaction: TransactionInterface}) => {
    return(
        <Dropdown className="d-inline mx-2" autoClose="outside">
            <Dropdown.Toggle id="dropdown-autoclose-outside">
            {transaction.title}
            </Dropdown.Toggle>
            <Dropdown.Menu>
                Hello world
            </Dropdown.Menu>
        </Dropdown>
    )
}

export default Transaction