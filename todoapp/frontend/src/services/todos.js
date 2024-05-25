import axios from 'axios'

class TodoDataService {
	getAll(token) {
		axios.defaults.headers.common['Authorization'] = 'Token ' + token
		return axios.get('https://localhost:8084/api/todos/')
	}

	createTodo(data, token) {
		axios.defaults.headers.common['Authorization'] = 'Token ' + token
		return axios.post('https://localhost:8084/api/todos/create/', data)
	}

	updateTodo(id, data, token) {
		axios.defaults.headers.common['Authorization'] = 'Token ' + token
		return axios.put(`https://localhost:8084/api/todos/${id}/`, data)
	}

	deleteTodo(id, token) {
		axios.defaults.headers.common['Authorization'] = 'Token ' + token
		return axios.delete(`https://localhost:8084/api/todos/${id}/`)
	}

	completeTodo(id, token) {
		axios.defaults.headers.common['Authorization'] = 'Token ' + token
		return axios.put(`https://localhost:8084/api/todos/${id}/complete/`)
	}

	login(data) {
		return axios.post('https://localhost:8084/api/login/', data)
	}

	signup(data) {
		return axios.post('https://localhost:8084/api/signup/', data)
	}
}

export default new TodoDataService()
