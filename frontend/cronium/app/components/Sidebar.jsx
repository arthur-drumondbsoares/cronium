import React from 'react'
import { FaClock, FaCalendarAlt } from "react-icons/fa";
import { AiFillProject } from "react-icons/ai";
import { VscSymbolMethod } from "react-icons/vsc";



import { Poppins } from 'next/font/google';

const poppins = Poppins({
  weight: ["600","800"],
  subsets: ["latin"],
})

//https://colorlib.com/wp/wp-content/uploads/sites/2/bootstrap-sidebar-170625.jpg
const Sidebar = () => {
  return (
    <div className={`w-44 h-full fixed bg-side-color border-2 border-black text-white ${poppins.className} `} >
        <div className='flex flex-col  '>
            <div className={`mb-8 font-bold text-3xl`}>
              <h1>Cronium</h1>
            
              

            </div>
            <div className='w-full h-16 p-3 flex items-center gap-4 hover:bg-side-hover'>
              <FaClock color='white'/>
              <div>Today</div>
            </div>
            <div className='w-full h-16 p-3 flex items-center gap-4 hover:bg-side-hover'>
              <FaCalendarAlt color='white'/>
              <div>Calendar</div>
            </div>
            <div className='w-full h-16 p-3 flex items-center gap-4 hover:bg-side-hover'>
              <AiFillProject color='white'/>
              <div>Projects</div>
            </div>
            <div className='w-full h-16 p-3 flex items-center gap-4 hover:bg-side-hover'>
              <VscSymbolMethod/>
              <div>Method</div>
            </div>
        </div>
        

    </div>
  )
}

export default Sidebar