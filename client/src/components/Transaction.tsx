import { TransactionInterface } from "./../classes";
const Transaction = ({transaction} : {transaction: TransactionInterface}) => {
    return(<>
            {transaction.title}
            </>
    )
}

export default Transaction