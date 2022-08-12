import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import Button from '@mui/material/Button'
import {useState, useCallback} from 'react'

const Home = (props) => {
  const [location, setLocation] = useState('')
  const [data, setData] = useState({})
  const [status, setStatus] = useState('')

  const getData = useCallback(() => {
    setStatus('Loading')
    const requestOptions = {
      method: 'POST',
    }
    fetch(`http://127.0.0.1:8000/locations/${location}`, requestOptions)
      .then(res => {
        if (!res.ok) {
          throw new Error()
        } 
        return res.json()
      })
      .then(data => setData(data))
      .then(() => setStatus('Success'))
      .catch(() => setStatus('Error'))
  }, [location])

  const handleChange = (e) => {
    setLocation(e.target.value)
    console.log(location)
  }

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
      <Box sx={{display: 'inline-flex'}}>
        <TextField sx={{m: 2}} placeholder='Enter your location' onChange={handleChange}/>
        <Button sx={{m: 2}} variant="contained" onClick={getData}>Search</Button>
      </Box>
      <Box>
        {status === 'Loading' && <div>Loading...</div>}
        {status === 'Error' && <div>Sorry, area type or area name not recognised.</div>}
        {status === 'Success' && <Box sx={{ typography: 'h2' }}>{data.cases}</Box>}
    </Box>
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
