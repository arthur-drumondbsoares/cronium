'use client'
import dayjs from "dayjs";
import { makeDate, months } from "../utils/calendar";
import { use, useEffect, useState } from "react";
import { GrFormNext, GrFormPrevious } from "react-icons/gr";
import  generate  from "../utils/generate";
import { useDataContext } from "../context/data";
import axios from 'axios'
import CalendarTask from "./CalendarTask";




export default function Calendar() {
  const days = ["S","M","T","W","T","F","S"]
  const current = dayjs()
  const [today, setToday] = useState(current)
  const [selectDate, setSelectDate] = useState(current);
  const [isLoading, setIsLoading] = useState(true)

  const {data, setData} = useDataContext()

  const fetchData = async ()=>{
    const response = await axios.get('http://127.0.0.1:8000/api/1')
    await setData(response.data)
    setIsLoading(false)
   
   
   }

  useEffect(()=>{

    fetchData()
    
  },[])

  return (
    
  
  <>
  {isLoading ? (
    <div>
      <h1>Loading</h1>
    </div>
  ): ( 
  
   <div className=" w-full h-full flex items-start justify-start">


    <div className="w-1/2 h-96 ">
      <div className="flex justify-between">
       <h1 className="font-bold text-purple-tint">{months[today.month()]} {today.year()}</h1>
       <div className="flex gap-2 items-center">
          <GrFormPrevious
                  className="w-5 h-5 cursor-pointer hover:scale-105 transition-all"
                  onClick={() => {
                    setToday(today.month(today.month() - 1));
                  }}
                />
                <h1
                  className=" cursor-pointer hover:scale-105 transition-all font-light"
                  onClick={() => {
                    setToday(currentDate);
                  }}
                >
                  {selectDate.toDate().toDateString().replace(" ", ", ")}
                </h1>
                <GrFormNext
                  className="w-5 h-5 cursor-pointer hover:scale-105 transition-all"
                  onClick={() => {
                    setToday(today.month(today.month() + 1));
                  }}
                />
          </div>
      </div>
      
      <div className="w-full grid grid-cols-7">
        {days.map((day, index)=>{
          return <h1 key={index} className="text-center">{day}</h1>
        })}
      </div>

      <div className="w-full grid grid-cols-7 ">
        {makeDate(today.month(), today.year()).map(({date, currentMonth, today}, index)=>{
          let hasTaskIndicator = false

          return (
          <>
            



            <div className="h-14 border-t grid place-content-center p-10" key={index}>
              
              {data.tasks.map((task, index)=>{
                
                if (task.date == date.format("YYYY-MM-DD")) {
                  if (!hasTaskIndicator){
                  hasTaskIndicator = true
                  return <div className="relative w-2 h-2 rounded-full bg-purple-500 top-0.1" key={index}></div>
                  }}
              })}
              <h1 key={index}
                className={generate(

                    currentMonth ? "" : "text-gray-400",
                    today
                        ? "bg-red-600 text-white"
                        : "",
                    selectDate
                        .toDate()
                        .toDateString() ===
                        date.toDate().toDateString()
                        ? "bg-black text-white"
                        : "",




                    "h-10 w-10 rounded-full grid place-content-center hover:bg-black hover:text-white transition-all cursor-pointer select-none",

                )} 

                onClick={() => {
                    setSelectDate(date);
                }}
            >
                {date.date()}</h1>
              
              
            </div>
          </>
          )
        })}

      </div>
      
    </div>


    <div className="  h-full w-1/2 ml-16 grid grid-cols-2">
        {
          data.tasks.filter(task => task.date == selectDate.format("YYYY-MM-DD"))
          .map((task, index) => {
            
            
            let projectTitle;
            let listTitle;
            if (task.list) {
              const project = data.projects.find(project => project.lists.some(list => list.id === task.list))
              if (project) {
                const list = project.lists.find(list => list.id === task.list)
                projectTitle = project.title
                listTitle = list ? list.title : ''
                console.log(project)
              }
            }
            
          
            
            return <CalendarTask 
              key={task.id}
              title={task.title}
              description={task.description}
              time={task.time}
              status={task.status}
              flag={task.flag}
              project={projectTitle}
              list={listTitle}
             

            />
          })
          
          
        }
        

        
    </div>
    



   </div>)}
  </>



  

  );
}
