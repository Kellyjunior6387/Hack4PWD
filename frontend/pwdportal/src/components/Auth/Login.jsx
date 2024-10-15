import React, { useState} from 'react'

const Login = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState ("")
    const [role, setRole] = useState("");

    const [isAuthorized, setIsAuthorized] = useContext(Context);

    const handleLogin = async (e)=> {
        e.preventDefault();
        try {
            const { data } = await 
        }
    };

  return (
    <div>
      
    </div>
  )
}

export default Login
