import React, { useRef, useMemo, useEffect } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Points, PointMaterial } from '@react-three/drei';
import * as THREE from 'three';
import './GalaxyBackground.css';

// Galaxy Stars Component
function GalaxyStars() {
  const ref = useRef();
  
  // Generate random stars with varying sizes and positions
  const [positions, colors, sizes] = useMemo(() => {
    const positions = new Float32Array(15000 * 3); // 15,000 stars
    const colors = new Float32Array(15000 * 3);
    const sizes = new Float32Array(15000);
    
    for (let i = 0; i < 15000; i++) {
      // Random positions in a large sphere
      const radius = Math.random() * 2000 + 500;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(2 * Math.random() - 1);
      
      positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
      positions[i * 3 + 2] = radius * Math.cos(phi);
      
      // Random star colors with enhanced brightness and glare
      const colorVariation = Math.random();
      const brightness = 0.7 + Math.random() * 0.3; // Enhanced brightness
      const baseColor = new THREE.Color();
      baseColor.setHSL(0.6 + colorVariation * 0.1, 0.2 + colorVariation * 0.3, brightness);
      
      colors[i * 3] = baseColor.r;
      colors[i * 3 + 1] = baseColor.g;
      colors[i * 3 + 2] = baseColor.b;
      
      // Random star sizes with proper distribution (90% below 0.7px, max 1.5px)
      const rand = Math.random();
      if (rand < 0.9) {
        sizes[i] = Math.random() * 0.4 + 0.1; // 90% of stars: 0.1-0.5px
      } else {
        sizes[i] = Math.random() * 0.5 + 0.5; // 10% of stars: 0.5-1.0px
      }
      sizes[i] = Math.min(sizes[i], 0.75); // Max 1.5px diameter (0.75px radius)
    }
    
    return [positions, colors, sizes];
  }, []);
  
  useFrame((state) => {
    if (ref.current) {
      ref.current.rotation.x = state.clock.elapsedTime * 0.01;
      ref.current.rotation.y = state.clock.elapsedTime * 0.005;
    }
  });
  
  return (
    <Points ref={ref} positions={positions} colors={colors} sizes={sizes} stride={3} frustumCulled={false}>
      <PointMaterial
        transparent
        color="#ffffff"
        size={1}
        sizeAttenuation={true}
        depthWrite={false}
        vertexColors={true}
        vertexSizes={true}
        blending={THREE.AdditiveBlending}
      />
    </Points>
  );
}

// Nebula Clouds Component
function NebulaClouds() {
  const ref = useRef();
  
  const [positions, colors] = useMemo(() => {
    const positions = new Float32Array(5000 * 3);
    const colors = new Float32Array(5000 * 3);
    
    for (let i = 0; i < 5000; i++) {
      // Create nebula-like cloud formations
      const radius = Math.random() * 1000 + 200;
      const theta = Math.random() * Math.PI * 2;
      const phi = Math.acos(2 * Math.random() - 1);
      
      positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
      positions[i * 3 + 2] = radius * Math.cos(phi);
      
      // Nebula colors (purple, blue, pink)
      const colorChoice = Math.random();
      let baseColor;
      if (colorChoice < 0.33) {
        baseColor = new THREE.Color(0.5, 0.2, 0.8); // Purple
      } else if (colorChoice < 0.66) {
        baseColor = new THREE.Color(0.2, 0.4, 0.8); // Blue
      } else {
        baseColor = new THREE.Color(0.8, 0.3, 0.6); // Pink
      }
      
      colors[i * 3] = baseColor.r;
      colors[i * 3 + 1] = baseColor.g;
      colors[i * 3 + 2] = baseColor.b;
    }
    
    return [positions, colors];
  }, []);
  
  useFrame((state) => {
    if (ref.current) {
      ref.current.rotation.x = state.clock.elapsedTime * 0.002;
      ref.current.rotation.z = state.clock.elapsedTime * 0.001;
    }
  });
  
  return (
    <Points ref={ref} positions={positions} colors={colors} stride={3} frustumCulled={false}>
      <PointMaterial
        transparent
        color="#ffffff"
        size={2}
        sizeAttenuation={true}
        depthWrite={false}
        vertexColors={true}
        blending={THREE.AdditiveBlending}
        opacity={0.3}
      />
    </Points>
  );
}

// Shooting Stars Component
function ShootingStars() {
  const [shootingStars, setShootingStars] = React.useState([]);
  
  useEffect(() => {
    const createShootingStar = () => {
      if (Math.random() < 0.2) { // increase frequency
        const newStar = {
          id: Date.now() + Math.random(),
          startPosition: [
            (Math.random() - 0.5) * 2000,
            (Math.random() - 0.5) * 2000,
            (Math.random() - 0.5) * 2000
          ],
          endPosition: [
            (Math.random() - 0.5) * 2000,
            (Math.random() - 0.5) * 2000,
            (Math.random() - 0.5) * 2000
          ],
          duration: 2 + Math.random() * 3,
          delay: Math.random() * 2
        };
        
        setShootingStars(prev => [...prev, newStar]);
        
        setTimeout(() => {
          setShootingStars(prev => prev.filter(star => star.id !== newStar.id));
        }, (newStar.duration + newStar.delay) * 1000);
      }
    };
    
    const interval = setInterval(createShootingStar, 1500);
    return () => clearInterval(interval);
  }, []);
  
  return (
    <group>
      {shootingStars.map(star => (
        <ShootingStar key={star.id} star={star} />
      ))}
    </group>
  );
}

// Individual Shooting Star Component
function ShootingStar({ star }) {
  const [progress, setProgress] = React.useState(0);
  const trailRef = useRef();
  
  useEffect(() => {
    const startTime = Date.now() + star.delay * 1000;
    const duration = star.duration * 1000;
    
    const animate = () => {
      const elapsed = Date.now() - startTime;
      if (elapsed >= 0) {
        const newProgress = Math.min(elapsed / duration, 1);
        setProgress(newProgress);
        
        if (newProgress < 1) {
          requestAnimationFrame(animate);
        }
      } else {
        requestAnimationFrame(animate);
      }
    };
    
    requestAnimationFrame(animate);
  }, [star.delay, star.duration]);
  
  const currentPosition = [
    star.startPosition[0] + (star.endPosition[0] - star.startPosition[0]) * progress,
    star.startPosition[1] + (star.endPosition[1] - star.startPosition[1]) * progress,
    star.startPosition[2] + (star.endPosition[2] - star.startPosition[2]) * progress
  ];
  
  const opacity = progress < 0.1 ? progress * 10 : progress > 0.9 ? (1 - progress) * 10 : 1;
  
  // Calculate trail direction
  const direction = [
    star.endPosition[0] - star.startPosition[0],
    star.endPosition[1] - star.startPosition[1],
    star.endPosition[2] - star.startPosition[2]
  ];
  
  // Normalize direction
  const length = Math.sqrt(direction[0] ** 2 + direction[1] ** 2 + direction[2] ** 2);
  const normalizedDirection = [direction[0] / length, direction[1] / length, direction[2] / length];
  
  return (
    <group position={currentPosition}>
      {/* Main shooting star with glow */}
      <mesh>
        <sphereGeometry args={[0.3, 8, 8]} />
        <meshBasicMaterial
          color="#ffffff"
          transparent
          opacity={opacity}
          blending={THREE.AdditiveBlending}
        />
      </mesh>
      {/* Core glow */}
      <mesh>
        <sphereGeometry args={[0.6, 8, 8]} />
        <meshBasicMaterial
          color="#60a5fa"
          transparent
          opacity={opacity * 0.4}
          blending={THREE.AdditiveBlending}
        />
      </mesh>
      {/* Outer glow */}
      <mesh>
        <sphereGeometry args={[1.0, 8, 8]} />
        <meshBasicMaterial
          color="#a78bfa"
          transparent
          opacity={opacity * 0.2}
          blending={THREE.AdditiveBlending}
        />
      </mesh>
      {/* Cone-shaped trail */}
      <mesh ref={trailRef} position={[-normalizedDirection[0] * 2, -normalizedDirection[1] * 2, -normalizedDirection[2] * 2]}>
        <coneGeometry args={[0.8, 4, 8]} />
        <meshBasicMaterial
          color="#ffffff"
          transparent
          opacity={opacity * 0.3}
          blending={THREE.AdditiveBlending}
          side={THREE.DoubleSide}
        />
      </mesh>
      {/* Trail glow */}
      <mesh position={[-normalizedDirection[0] * 2, -normalizedDirection[1] * 2, -normalizedDirection[2] * 2]}>
        <coneGeometry args={[1.2, 5, 8]} />
        <meshBasicMaterial
          color="#60a5fa"
          transparent
          opacity={opacity * 0.15}
          blending={THREE.AdditiveBlending}
          side={THREE.DoubleSide}
        />
      </mesh>
    </group>
  );
}

// Main Galaxy Background Component
const GalaxyBackground = () => {
  return (
    <div className="galaxy-background">
      <Canvas
        camera={{ position: [0, 0, 1000], fov: 75 }}
        style={{ background: 'transparent' }}
        gl={{ alpha: true, antialias: true }}
      >
        <ambientLight intensity={0.1} />
        <pointLight position={[10, 10, 10]} intensity={0.5} />
        
        <GalaxyStars />
        <NebulaClouds />
        <ShootingStars />
      </Canvas>
    </div>
  );
};

export default GalaxyBackground;
