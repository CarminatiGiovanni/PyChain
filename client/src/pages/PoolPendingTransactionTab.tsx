import { useContext, useEffect, useState } from "react"
import { Button } from "react-bootstrap"
import { BlockchainContext } from "../App"
import { TransactionInterface } from "../classes"
import Transaction from "../components/Transaction"

const PoolPendingTransactionTab = () => {
    const {blockchain} = useContext(BlockchainContext)
    const [transactionPool, setTransactionPool] = useState<{"transaction's pool":TransactionInterface[]}>({'transaction\'s pool':[]})

    const reload = () => {
        
        fetch(blockchain?.address + '/diagnostic/transaction_pool', {
            method: 'GET'
        }).then(res => res.json()).then(json => {
            setTransactionPool(json)}).catch(e => console.log(e.message))
    }

    return (
        <>
            <Button variant="danger" onClick={reload}>Click</Button>
            {
                (transactionPool["transaction's pool"] as TransactionInterface[]).map((t,index) => {
                    return <Transaction transaction={t} key={index}/>
                })
            }
        </>
    )
}

export default PoolPendingTransactionTab