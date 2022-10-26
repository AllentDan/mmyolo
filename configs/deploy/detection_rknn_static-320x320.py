_base_ = ['./base_static.py']
onnx_config = dict(
    input_shape=[320, 320], output_names=['feat0', 'feat1', 'feat2'])
use_efficientnms = False
codebase_config = dict(model_type='rknn')
backend_config = dict(
    type='rknn',
    common_config=dict(
        mean_values=None,  # [[0, 0, 0]],
        std_values=None,  # [[255, 255, 255]],
        target_platform='rv1126',
        optimization_level=1),
    quantization_config=dict(do_quantization=False, dataset=None),
    input_size_list=[[3, 320, 320]])
