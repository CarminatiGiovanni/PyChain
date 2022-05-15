import { TransactionInterface } from "./../classes";
import Transaction from "./Transaction";

const TransactionList = ({transactions} : {transactions: TransactionInterface[]}) => {
    return(
        <div className="d-grid gap-2">
            {
                    transactions.map((t,index) => {
                    const {author,value,title,timestamp} = t
                    return(
                        <Transaction key={index} transaction={t} />
                    )
                })
            }
       </div>
    )
}

export default TransactionList