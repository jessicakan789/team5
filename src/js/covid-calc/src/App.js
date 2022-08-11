import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import Button from '@mui/material/Button'
import logo from './logo.svg'
import {useState, useEffect} from 'react'

const Home = (props) => {
  const [location, setLocation] = useState('')
  const [data, setData] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [err, setErr] = useState('');
  const handleChange = (e) => setLocation(e.target.value)
  const handleClickEvent = () => setIsLoading(!isLoading)
  return (
    <Box sx={{
      width: '100vw', 
      height: '100vh',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
      alignItems: 'center',
    }}>
      <Box sx={{ typography: 'h2' }}>COVID-19 Risk Calculator</Box>
      <Box>Image Here</Box>
      <Box>
        <TextField placeholder='Enter your location' onChange={handleChange}/>
        <Button variant="contained" onClick={handleClickEvent}>Button</Button>
      </Box>
      {isLoading ? <Results location={location}/> : <></>}
      
    </Box>
  )
}

const Results = (props) => {
  const [data, setData] = useState({})
  useEffect(() => {
    const requestOptions = {
      method: 'POST',
      mode: 'no-cors'
    }
    fetch(`http://127.0.0.1:8000/locations/${props.location}`, requestOptions)
      .then(res => res.json())
      .then(data => setData(data))
  }, [])

  return (
    <Box sx={{ typography: 'h2' }}>
      {data && data.cases}
    </Box>
  )
}

function App() {
  return (
    <Box sx={{
      backgroundColor: 'green', 
    }}>
      <Home />
    </Box>
  )
}

export default App;
