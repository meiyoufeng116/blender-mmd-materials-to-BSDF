import bpy
for material in bpy.data.materials:
    if material.node_tree.nodes.get("mmd_shader"):
        material.node_tree.nodes.remove(material.node_tree.nodes["mmd_shader"])
        if material.node_tree.nodes.get("mmd_toon_tex"):
            material.node_tree.nodes.remove(material.node_tree.nodes["mmd_toon_tex"])
        if material.node_tree.nodes.get("mmd_sphere_tex"):
            material.node_tree.nodes.remove(material.node_tree.nodes["mmd_sphere_tex"])
        material.node_tree.nodes.new("ShaderNodeBsdfPrincipled")
        material.node_tree.nodes["原理化BSDF"].location=[100,1400]
        link=material.node_tree.links
        node=material.node_tree.nodes
        if material.node_tree.nodes.get('mmd_base_tex'):
            link.new(node['mmd_base_tex'].outputs['Color'],node['原理化BSDF'].inputs['Base Color'])
            link.new(node['mmd_base_tex'].outputs['Alpha'],node['原理化BSDF'].inputs['Alpha'])
        link.new(node['原理化BSDF'].outputs['BSDF'],node["材质输出"].inputs['Surface'])


