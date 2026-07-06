import { useState } from "react";

function useApi() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  return {
    loading,
    setLoading,
    error,
    setError
  };
}

export default useApi;