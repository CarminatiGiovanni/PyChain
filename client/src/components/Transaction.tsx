import { TransactionInterface } from "./../classes";
import { Button } from "react-bootstrap";
const Transaction = ({transaction} : {transaction: TransactionInterface}) => {
    return(
        
            <Button variant={randColor()} size="lg" disabled>
                {transaction.title}
            </Button>
        
    )
}

export default Transaction

function randColor() : string{
    const colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
    
    const n = Math.floor(Math.random() * colors.length) 

    return colors[n]
}