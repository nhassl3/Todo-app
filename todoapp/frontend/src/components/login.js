import React, { useState } from 'react'
import Form from 'react-bootstrap/Form'
import Container from 'react-bootstrap/Container'
import Button from 'react-bootstrap/Button'

const Login = props => {
	const [username, setUsername] = useState('')
	const [password, setPassword] = useState('')

	const onChangeUsername = e => {
		setUsername(e.target.value)
	}

	const onChangePassword = e => {
		setPassword(e.target.value)
	}

	const login = () => {
		props.login({ username: username, password: password })
		props.history.push('/')
	}

	return (
		<Container>
			<Form>
				<Form.Group className='mb-3'>
					<Form.Label>Username</Form.Label>
					<Form.Control
						type='text'
						placeholder='Enter username'
						value={username}
						onChange={onChangeUsername}
					/>
				</Form.Group>
				<Form.Group className='mb-3'>
					<Form.Label>Password</Form.Label>
					<Form.Control
						type='password'
						placeholder='Enter password'
						value={password}
						onChange={onChangePassword}
					/>
				</Form.Group>
				<Button variant='primary' onClick={login}>
					Login
				</Button>
			</Form>
		</Container>
	)
}

export default Login
