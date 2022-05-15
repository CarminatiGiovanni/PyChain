export interface TransactionInterface{
    content_type: string,
    author: string,
    title: string,
    value: string,
    description: string,
    timestamp: number
}

export interface BlockInterface{
  index: number,
  hash: string,
  transactions: TransactionInterface[],
  nonce: number,
  prevHash: string,
  timestamp: number
}

export interface BlockchainJSONInterface {
  blockchain: BlockInterface[]
}

