import React from 'react'

const EditWindow = ({isOpen}) => {
  return (
    <>
        
        <div className={`h-30 w-40 bg-blue-500 text-center ${isOpen? 'visible': 'hidden'}`}>
            Hello world
        </div>
    
    </>
  )
}

export default EditWindow