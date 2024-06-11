import React, { useState } from 'react';

const DraggableComponent = () => {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [dragging, setDragging] = useState(false);

  const handleMouseDown = (e) => {
    setDragging(true);
    setPosition({
      x: e.clientX,
      y: e.clientY
    });
  };

  const handleMouseMove = (e) => {
    if (dragging) {
      const deltaX = e.clientX - position.x;
      const deltaY = e.clientY - position.y;
      setPosition({
        x: position.x + deltaX,
        y: position.y + deltaY
      });
    }
  };

  const handleMouseUp = () => {
    setDragging(false);
  };

  return (
    <div
      style={{ position: 'absolute', left: position.x, top: position.y, cursor: dragging ? 'grabbing' : 'grab' }}
      onMouseDown={handleMouseDown}
      onMouseMove={handleMouseMove}
      onMouseUp={handleMouseUp}
    >
      <div style={{ width: '100px', height: '100px', background: 'lightblue', border: '1px solid blue' }}>
        Drag Me
      </div>
    </div>
  );
};

export default DraggableComponent;
