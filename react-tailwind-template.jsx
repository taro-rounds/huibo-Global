// 这是一个React + Tailwind CSS模板文件
// 请将您的React + Tailwind CSS代码粘贴到这里
import React from 'react';
import ReactDOM from 'react-dom/client';

function App() {
  return (
    <div className="bg-blue-50 min-h-screen flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg">
        <h1 className="text-2xl font-bold text-blue-600">React + Tailwind CSS Template</h1>
        <p className="mt-2 text-gray-600">请将您的代码粘贴到这个文件中</p>
      </div>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);