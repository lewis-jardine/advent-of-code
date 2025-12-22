package main

import (
	"reflect"
	"testing"
)

// func parseIdRange()
func TestParseIdRangeValid(t *testing.T) {
	out, err := parseIdRange("1234-5678")
	exp := Range{start: 1234, end: 5678}
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
	if err != nil {
		t.Errorf("recieved error: %v", err)
	}
}

func TestParseIdRangeInvalid(t *testing.T) {
	_, err := parseIdRange("1234-5678-6475")
	if err == nil {
		t.Error("expected error but recieved none")
	}
}

// func mergeRanges()
func TestMergeRangesIntersecting(t *testing.T) {
	ranges := []Range{{start: 1, end: 3}, {start: 3, end: 6}, {start: 4, end: 7}}
	out := mergeRanges(ranges)
	exp := []Range{{start: 1, end: 7}}
	if !reflect.DeepEqual(out, exp) {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestMergeRangesNotIntersecting(t *testing.T) {
	ranges := []Range{{start: 1, end: 2}, {start: 3, end: 6}}
	out := mergeRanges(ranges)
	if !reflect.DeepEqual(out, ranges) {
		t.Errorf("expected: %v	recieved: %v", ranges, out)
	}
}

// func orderRanges()
func TestOrderRanges(t *testing.T) {
	ranges := []Range{{start: 3, end: 6}, {start: 1, end: 2}, {start: 3, end: 7}}
	orderRanges(ranges)
	exp := []Range{{start: 1, end: 2}, {start: 3, end: 6}, {start: 3, end: 7}}
	if !reflect.DeepEqual(ranges, exp) {
		t.Errorf("expected: %v	recieved: %v", exp, ranges)
	}
}

// func rangesIntersect()
func TestRangesIntersectingPartial(t *testing.T) {
	out := rangesIntersect(Range{5, 7}, Range{4, 7})
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

// One range contains the other
func TestRangesIntersectingFull(t *testing.T) {
	out := rangesIntersect(Range{4, 7}, Range{5, 6})
	exp := true
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

func TestRangesIntersectingNot(t *testing.T) {
	out := rangesIntersect(Range{1, 3}, Range{4, 7})
	exp := false
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}

// func countRange()
func TestCountRange(t *testing.T) {
	out := countRange(Range{start: 4, end: 6})
	exp := 3
	if out != exp {
		t.Errorf("expected: %v	recieved: %v", exp, out)
	}
}
