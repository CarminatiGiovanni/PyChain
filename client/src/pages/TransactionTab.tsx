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
                        <>
                            {
                                b.transactions.map((t: TransactionInterface) => {
                                    return (
                                        <Transaction transaction={t} />
                                    )
                                })
                            }
                        </>
                    )
                })
            }
        </>
    )
}

export default TransactionTab