import { TransactionInterface } from "./../classes";
import TransactionPreview from "./TransactionPreview";

const TransactionList = ({transactions} : {transactions: TransactionInterface[]}) => {
    return(
        <div className="d-grid gap-2">
            {
                    transactions.map((t,index) => {
                    return(
                        <TransactionPreview key={index} transaction={t} />
                    )
                })
            }
       </div>
    )
}

export default TransactionList