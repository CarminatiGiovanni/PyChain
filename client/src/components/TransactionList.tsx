import { TransactionInterface } from "./../classes";

const TransactionList = ({transactions} : {transactions: TransactionInterface[]}) => {
    return(
        <>
       {
            transactions.map((t,index) => {
               const {author,value,title,timestamp} = t
               return(
                   <p key={index}>a</p>
               )
           })
       }
       </>
    )
}

export default TransactionList