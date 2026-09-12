"""Finite controls for the tag/stream note, not a proof of infinite omniscience.
Standard library only. Does not import project code or access the network.
"""
from itertools import product

def tagged_values(horizon):
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    yield ("none",)
    for n in range(horizon):
        for tail in product((0, 1), repeat=horizon-n-1):
            yield ("first", n, tail)

def encode_finite(value, horizon):
    if value[0] == "none":
        return (0,) * horizon
    _, n, tail = value
    if not 0 <= n < horizon or len(tail) != horizon-n-1:
        raise ValueError("invalid finite tagged value")
    return (0,) * n + (1,) + tail

def decode_finite(bits):
    for i, bit in enumerate(bits):
        if bit not in (0, 1):
            raise ValueError("invalid bit")
        if bit == 1:
            return ("first", i, bits[i+1:])
    return ("none",)

def run_checks(max_horizon=10):
    if not isinstance(max_horizon, int) or not 0 <= max_horizon <= 12:
        raise ValueError("max_horizon must be in 0..12")
    rows = []
    total_inputs = 0
    for k in range(max_horizon+1):
        encodings = {}
        tagged = list(tagged_values(k))
        assert len(tagged) == 2**k
        for t in tagged:
            b = encode_finite(t,k)
            assert b not in encodings
            encodings[b]=t
            assert decode_finite(b)==t
            assert int(t[0] == "first")==int(any(b))
        for b in product((0,1),repeat=k):
            assert encode_finite(decode_finite(b),k)==b
        assert len(encodings)==2**k
        rows.append({"horizon":k,"tagged_inputs":len(tagged),
                     "unique_images":len(encodings),
                     "left_inverse":True,"right_inverse":True})
        total_inputs += len(tagged)

    # Each finite zero transcript is compatible with a single spike outside it.
    # These are example transcripts, not enumeration of all infinite algorithms.
    transcript_cases = 0
    for mask in range(1<<max_horizon):
        queries = [i for i in range(max_horizon) if mask & (1<<i)]
        m = max(queries,default=-1)+1
        zero_answers = [0 for _ in queries]
        spike_answers = [int(k==m) for k in queries]
        assert zero_answers==spike_answers
        assert m not in queries
        transcript_cases += 1
    delayed_examples=0
    for inspected_prefix in range(65):
        m=inspected_prefix
        assert all(int(k==m)==0 for k in range(inspected_prefix))
        assert int(m==m)==1
        delayed_examples += 1

    # Deliberately horizon-bounded detector: good for finite input,
    # wrong if promoted to a general infinite-stream decision procedure.
    false_zero_examples=0
    for budget in range(65):
        hidden_spike=budget
        seen=[int(k==hidden_spike) for k in range(budget)]
        assert not any(seen)
        assert int(hidden_spike==hidden_spike)==1
        false_zero_examples+=1

    # Positive control: a preserved header answers the tag in one query.
    safe_header_cases=0
    for k in range(max_horizon+1):
        for t in tagged_values(k):
            safe=(0,) if t[0]=="none" else (1,)+(0,)*t[1]+(1,)+t[2]
            assert safe[0]==int(t[0]=="first")
            safe_header_cases+=1
    # Finite counterpart of unique image fibers. This does NOT simulate
    # HoTT's proof-relevant treatment of a truncated existence proof.
    k=max_horizon
    fibers={}
    for t in tagged_values(k):
        b=encode_finite(t,k)
        fibers.setdefault(b,[]).append(t)
    assert all(len(fiber)==1 for fiber in fibers.values())
    unique_fibers_checked=len(fibers)
    return {
      "status":"PASS_FINITE_SANITY_ONLY",
      "max_horizon":max_horizon,
      "finite_tagged_inputs_total":total_inputs,
      "horizon_results":rows,
      "finite_transcript_pairs":transcript_cases,
      "delayed_spike_examples":delayed_examples,
      "finite_detector_wrong_on_hidden_spike_examples":false_zero_examples,
      "safe_header_inputs_checked":safe_header_cases,
      "finite_unique_fibers_checked":unique_fibers_checked,
      "check_groups":[
        "finite_sum_cardinality","finite_encoding_injective",
        "finite_encoding_left_inverse","finite_encoding_right_inverse",
        "finite_tag_commutes","finite_zero_transcript_spike_pair",
        "arbitrary_tested_prefix_has_unseen_spike",
        "finite_detector_not_an_infinite_decider",
        "preserved_header_answers_tag", "finite_unique_image_fibers"],
      "not_established":[
        "The infinite theorem by finite enumeration",
        "LPO or WLPO independence",
        "HoTT kernel verification",
        "Computer-program source-inspection impossibility",
        "Physical nonrealizability without specified interface"]
    }
