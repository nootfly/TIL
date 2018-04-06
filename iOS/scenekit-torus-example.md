# SceneKit torus example

```swift
import UIKit
import SceneKit
import PlaygroundSupport

var sceneView = SCNView(frame:CGRect(x: 0, y: 0,width: 400, height: 400))
var scene = SCNScene()
sceneView.scene = scene
PlaygroundPage.current.liveView = sceneView


var cameraNode = SCNNode()
cameraNode.camera = SCNCamera()
cameraNode.position = SCNVector3(x: 0, y: 0, z: 4)
scene.rootNode.addChildNode(cameraNode)

var torus = SCNTorus(ringRadius: 1, pipeRadius: 0.35)
var torusNode = SCNNode(geometry: torus)
torusNode.position = SCNVector3(x: 0.0, y: 0.0, z: 0.0)
scene.rootNode.addChildNode(torusNode)

torus.firstMaterial?.diffuse.contents = UIColor.green
torus.firstMaterial?.specular.contents = UIColor.white

torusNode.rotation = SCNVector4(x: 1.0, y: 0.0, z: 0.0, w: Float(Double.pi/4.0))

var light = SCNLight()
light.type = SCNLight.LightType.spot
var lightNode = SCNNode()
lightNode.light = light
lightNode.position = SCNVector3(x: 0, y: 0, z: 6)
scene.rootNode.addChildNode(lightNode)

let moveAction = SCNAction.sequence([
    SCNAction.moveBy(x: -2, y: 0, z: 0, duration: 1),
    SCNAction.moveBy(x: 2, y: 0, z: 0, duration: 1),
    SCNAction.moveBy(x: 2, y: 0, z: 0, duration: 1),
    SCNAction.moveBy(x: -2, y: 0, z: 0, duration: 1)
    ])
lightNode.runAction(SCNAction.repeatForever(moveAction))

let rotateAction = SCNAction.rotate(by: CGFloat(Double.pi),
                                           around: SCNVector3(x: 1.0, y: 0.0, z: 0.0),
                                           duration: 4.0)

torusNode.runAction(SCNAction.repeatForever(rotateAction))
```

Reference: Swift: Developing iOS Applications