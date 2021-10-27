import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import { client } from '../../api/client'

const initialState = {
		num: 0,
		status: 'idle',
		error: null,
}


export const fetchNum = createAsyncThunk('nums/fetchNum', async () => {
		const response = await client.get('/nums/fetchNum')
		return response.data
})

export const updateNum = createAsyncThunk('nums/updateNum', async (body) => {
			const response = await client.post('/nums/updateNum', body)	
			return response.data
})

const numsSlice = createSlice({
	name: 'nums',
	initialState,
	extraReducers(builder){
		builder.addCase(fetchNum.fulfilled, (state, action) => {
			state.status = 'succeeded'
			console.log('payload:', action.payload)
			state.num = action.payload.num
		}).
			addCase(fetchNum.rejected, (state, action) => {
				state.status = 'failed'
				state.error = action.error.message
			})
			.addCase(updateNum.fulfilled, (state, action) => {
				console.log('payload.num:',action.payload.num)
				state.num = action.payload.num
			})
	}
})

export default numsSlice.reducer

export const selectNum = (state) => state.nums.num   // state.[name].item
