import { TransactionInterface } from "../classes";
import { Button } from "react-bootstrap";
const TransactionPreview = ({transaction} : {transaction: TransactionInterface}) => {
    return(
        
            <Button variant={randColor()} size="lg" disabled>
                {transaction.title}
            </Button>
        
    )
}

export default TransactionPreview

function randColor() : string{
    const colors = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'dark']
    
    const n = Math.floor(Math.random() * colors.length) 

    return colors[n]
}