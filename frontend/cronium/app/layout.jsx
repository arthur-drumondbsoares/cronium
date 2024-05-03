import "./globals.css";
import Sidebar from "./components/Sidebar";
import { DataContextProvider } from "./context/data";



export default function RootLayout({ children }) {
  return (
    <html>
      <body>
       <DataContextProvider>
          <div className="relative">

          
            <Sidebar />
            <div className=' ml-44 h-screen p-10 '>
              
                {children}
              

            </div>  

        
          </div>
        </DataContextProvider>
      </body>
    </html>

  );
}
