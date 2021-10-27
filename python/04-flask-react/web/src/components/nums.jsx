import * as React from 'react'
import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchNum, updateNum, selectNum } from '../features/num/numSlice'
import './nums.scss'

const Nums = () => {
	const dispatch = useDispatch()
	const num = useSelector(selectNum)
	useEffect(()=>{
		dispatch(fetchNum())
	},[])
	const addTen = () => {
		console.log("+ 10")
		dispatch(updateNum({action:'add', step:10}))
	}
  const divTen = () => {
		console.log("- 20")
		dispatch(updateNum({action:'div', step: 20}))
	}
	return (
		<div className='nums'>
			<span>{num}</span>
			<button onClick={()=>{addTen()}}>+ 10</button>
			<button onClick={()=>{divTen()}}>- 20</button>
		</div>	
	)
}

export default Nums
