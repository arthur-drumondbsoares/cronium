import React from 'react'
import { FaFlag } from "react-icons/fa";
import { LuClock10 } from "react-icons/lu";
import EditWindow from './EditWindow';
import { useState } from 'react'




const CalendarTask = ({title, description, time, status, flag, list, project}) => {
  
  return (
    
    <>
    
    <div class={`w-60 h-52 rounded pl-3 overflow-hidden shadow-lg animate-fade flex flex-col hover:scale-110 transition-all ease-in-out`}>
        
        
        <div>
            
              <p class="font-bold text-xl mb-2">{title}</p>
          

            {list && <p className='text-sm opacity-50 inline-block'>{project}: {list}</p>}

            <p class=" opacity-55 text-sm overflow-hidden">
            {description}
            </p>
            
            <p>{time}</p>
            <div className='text-sm opacity-70 flex items-center mt-12'>
                <FaFlag color='red' className='mr-2'/>
                <p>{flag}</p>
            </div>
            <div className='text-sm opacity-70 flex items-center'>
                <LuClock10 className='mr-2' />
                <p>{status}</p>
            </div>

            
        </div>


        
    </div>
    
    
    
    
    </>
  )
}

export default CalendarTask