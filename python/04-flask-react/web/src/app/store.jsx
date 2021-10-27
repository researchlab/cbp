import { configureStore } from '@reduxjs/toolkit'
import numsReducer from '../features/num/numSlice'


export default configureStore({
	reducer:{
		nums: numsReducer
	}
})
