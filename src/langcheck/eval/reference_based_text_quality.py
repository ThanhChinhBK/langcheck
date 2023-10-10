from __future__ import annotations

from typing import List, Optional

from langcheck.eval._validation import validate_parameters_reference_based
from langcheck.eval.eval_value import EvalValue


def exact_match(generated_outputs: List[str] | str,
                reference_outputs: List[str] | str,
                prompts: Optional[List[str] | str] = None) -> EvalValue[int]:
    '''Checks if the generated outputs exact matches with the reference outputs.
    This metric takes on binary 0 or 1 values.

    Args:
        generated_outputs: The model generated output(s) to evaluate
        reference_outputs: The reference output(s)
        prompts: The prompts used to generate the output(s). Prompts are
            optional metadata and not used to calculate the metric.

    Returns:
        An :class:`~langcheck.eval.eval_value.EvalValue` object
    '''
    generated_outputs, reference_outputs, prompts = validate_parameters_reference_based(
        generated_outputs, reference_outputs, prompts)

    # The values are binary: 1 if it's an exact match and 0 if not
    metric_values = []
    for gen, ref in zip(generated_outputs, reference_outputs):
        if gen == ref:
            metric_values.append(1)
        else:
            metric_values.append(0)

    return EvalValue(metric_name='exact_match',
                     prompts=prompts,
                     generated_outputs=generated_outputs,
                     reference_outputs=reference_outputs,
                     sources=None,
                     metric_values=metric_values,
                     language=None)
