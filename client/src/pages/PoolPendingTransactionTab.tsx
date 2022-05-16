import { useContext, useEffect, useState } from "react"
import { BlockchainContext } from "../App"
import { TransactionInterface } from "../classes"
import Transaction from "../components/Transaction"

const PoolPendingTransactionTab = () => {
    const {blockchain} = useContext(BlockchainContext)
    const [transactionPool, setTransactionPool] = useState<{"transaction's pool":TransactionInterface[]}>({'transaction\'s pool':[]})

    useEffect(() => {
        fetch(blockchain?.address + '/diagnostic/transaction_pool' || '', {
            method: 'GET'
        }).then(res => res.json()).then(json => {
            setTransactionPool(json)}).catch(e => console.log(e.message))
    }, [blockchain?.address])

    return (
        <>
            {
                (transactionPool["transaction's pool"] as TransactionInterface[]).map(t => {
                    return <Transaction transaction={t}/>
                })
            }
        </>
    )
}

export default PoolPendingTransactionTab