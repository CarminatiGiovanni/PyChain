import { strictEqual } from "assert"
import { useContext } from "react"
import { BlockchainContext } from "../App"
import { BlockInterface, TransactionInterface } from "../classes"
import Transaction from "../components/Transaction"

const TransactionTab = () => {
    const {blockchain} = useContext(BlockchainContext)
    return (
        <>
            {   
                blockchain?.blockchain.map((b: BlockInterface) => {
                    return(
                        <div key = {b.hash}>
                            {
                                b.transactions.map((t: TransactionInterface,index) => {
                                    return (
                                        <Transaction key={b.hash + '_' + index.toString()} transaction={t} />
                                    )
                                })
                            }
                        </div>
                    )
                })
            }
        </>
    )
}

export default TransactionTab