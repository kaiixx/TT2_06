import {userState} from 'react'

const AddExpense = () => {
    const [name,setName] = useState('')
    const [description, setDescription] = useState('')
    const [amount, setAmount] = useState(0)

    const onSubmit = (e) =>{
        e.preventDefault();

        onAdd ({name, description, amount})

        setName('')
        setDescription('')
        setAmount(0)
    }

    return (
        <form className='add-form' onSubmit={onSubmit}>
          <div className='form-control'>
            <label>Name</label>
            <input
              type='text'
              placeholder='Add Name of Expense'
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>
          <div className='form-control'>
            <label>Description</label>
            <input
              type='text'
              placeholder='Add Description of Expense'
              value={description}
              onChange={(e) => setDescription(e.target.value)}
            />
          </div>
          <div className='form-control'>
            <label>Amount</label>
            <input
              type='number'
              value={amount}
              onChange={(e) => setAmount(e.currentTarget.checked)}
            />
          </div>
    
          <input type='submit' value='Save Task' className='btn' />
        </form>
      )
    }

export default AddExpense
